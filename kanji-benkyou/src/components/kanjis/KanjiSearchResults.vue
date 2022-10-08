<template>
	<section>
		<a-alert
			v-if="!kanjis.length && !loading"
			type="warning"
			message="No results found"
			show-icon
		/>
		<template v-else>
			<h3>Showing {{ kanjis.length }} out of {{ total }}</h3>

			<a-pagination
				:current="page"
				:total="total"
				:pageSize="pageSize"
				:show-size-changer="false"
				@change="(pg) => $emit('page', pg)"
			/>

			<div class="kanjis-list">
				<a-spin size="large" v-if="loading" />
				<KanjiCard v-for="k in kanjis" :key="k.id" :kanji="k" />
			</div>

			<a-pagination
				:current="page"
				:total="total"
				:pageSize="pageSize"
				:show-size-changer="false"
				@change="(pg) => $emit('page', pg)"
			/>
		</template>
	</section>
</template>

<script>
import { ref } from 'vue';

import { PAGE_SIZE } from '@/api';
import KanjiCard from '@/components/kanjis/KanjiCard.vue';

export default {
	name: 'KanjiSearchResults',
	emits: ['page'],
	components: {
		KanjiCard,
	},
	props: {
		loading: {
			type: Boolean,
			required: true,
		},
		page: {
			type: Number,
			required: true,
		},
		total: {
			type: Number,
			required: true,
		},
		kanjis: {
			type: Array,
			required: true,
		},
	},
	data() {
		return {
			pageSize: PAGE_SIZE,
		};
	},
};
</script>

<style lang="scss">
.kanjis-list {
	display: flex;
	flex-wrap: wrap;
	justify-content: space-around;
	align-items: strech;
	margin-left: -15px;
}
</style>
