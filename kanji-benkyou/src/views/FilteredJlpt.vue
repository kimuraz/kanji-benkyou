<template>
	<div id="filtered-jlpt">
		<div class="filters">
			<JlptBadge
				v-for="lvl in 5"
				@click="!loading && getKanjis(lvl, 1)"
				:key="lvl"
				:level="lvl"
				:active="lvl === activeLevel"
			/>
		</div>

		<KanjiSearchResults
			@page="(pg) => getKanjis(activeLevel, pg)"
			:loading="loading"
			:page="page"
			:total="ttl"
			:kanjis="kanjis"
		/>
	</div>
</template>

<script>
import { reactive, toRefs, onMounted } from 'vue';
import JlptBadge from '@/components/kanjis/JlptBadge.vue';
import KanjiSearchResults from '@/components/kanjis/KanjiSearchResults.vue';

import api, { PAGE_SIZE } from '@/api';

export default {
	name: 'FilteredJlpt',
	components: {
		JlptBadge,
		KanjiSearchResults,
	},
	setup() {
		const state = reactive({
			activeLevel: 5,
			page: 1,
			kanjis: [],
			ttl: 0,
			loading: true,
		});

		const getKanjis = async (lvl, curPage = 1) => {
			state.kanjis = [];
			state.loading = true;
			try {
				const { data } = await api.get(
					`/kanjis/?jlpt=${lvl}&offset=${PAGE_SIZE * (curPage - 1)}`
				);
				state.activeLevel = lvl;
				state.page = curPage;
				state.kanjis = data.results;
				state.ttl = data.count;
			} catch (error) {
				console.log(error);
			} finally {
				state.loading = false;
			}
		};

		onMounted(() => {
			getKanjis(5);
		});

		return { getKanjis, ...toRefs(state) };
	},
};
</script>

<style lang="scss">
#filtered-jlpt {
	padding: 20px;
	.filters {
		margin-left: 20px;
		margin-bottom: 20px;
		> span {
			cursor: pointer;
		}
	}
}
</style>
